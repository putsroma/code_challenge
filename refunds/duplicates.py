"""Nightly check for refunds sent twice by mistake."""


def find_duplicates(refunds: list) -> list:
    """Refunds with the same merchant_id, amount_cents, card_last4 and day are duplicates.
    Return the ids of every refund after the first one in each group, in input order."""
    known_refund = set()
    duplicates = []
    for refund in refunds:
        key = (refund["merchant_id"], refund["amount_cents"], refund["card_last4"], refund["day"])
        if key in known_refund:
            duplicates.append(refund["id"])
        else:
            known_refund.add(key)
    return duplicates
