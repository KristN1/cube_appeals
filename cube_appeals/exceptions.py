class PlayerNeverJoined(ValueError):
    def __init__(self, player: str):
        self.player = player
        self.msg = f"Player {player} has never joined the server"
        ValueError.__init__(self, self.msg)

class RateLimited(ValueError):
    def __init__(self):
        self.msg = "You are being rate limited"
        ValueError.__init__(self, self.msg)

class AppealUrlUnavailable(ValueError):
    def __init__(self, player: str):
        self.player = player
        self.msg = f"Appeal url for {player} is unavailable, check the player appeal status"
        ValueError.__init__(self, self.msg)

class PlayerNotPunished(ValueError):
    def __init__(self, player: str):
        self.player = player
        self.msg = f"Player {player} is not currently punished"
        ValueError.__init__(self, self.msg)