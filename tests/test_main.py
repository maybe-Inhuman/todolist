from main import main


class TestMain:
    def test_returns_none(self) -> None:
        assert main() == None

    def test_name(self) -> None:
        assert main.__name__ == "main"
