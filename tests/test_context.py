from fluent_logger import FluentLogger

def test_adding_context_sets_value():
    f = FluentLogger()
    f.with_context("test", "value")
    assert f.get_context("test") == "value"
    
def test_removing_context_removes_value():
    f = FluentLogger()
    f.with_context("test", "value")
    assert not f.without_context("test").get_context("test")

