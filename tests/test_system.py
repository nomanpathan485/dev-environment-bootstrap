from src.devenv.system import check_tool

def test_check_tool_with_python():
    result = check_tool("python")
    assert result is not None

def test_check_tool_with_fake_tool():
    result = check_tool("definitely_not_a_real_tool_12345")
    assert result is None