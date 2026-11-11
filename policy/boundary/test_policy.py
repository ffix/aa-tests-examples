from policy_mutant import can_publish

def test_can_publish_at_18():
    assert can_publish(18) is True

def test_cannot_publish_at_17():
    assert can_publish(17) is False
