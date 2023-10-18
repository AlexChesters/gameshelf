from django.db import models

game_platforms = [
    # PC
    ("steam", "Steam"),
    ("epic", "Epic"),
    ("xbox_pc", "Xbox (PC)"),
    ("gog_galaxy", "GOG Galaxy"),
    ("pc_standalone", "PC (standalone)"),
    # Xbox
    ("xbox_og", "Xbox (original)"),
    ("xbox_360", "Xbox 360"),
    ("xbox_one", "Xbox One"),
    ("xbox_one_s", "Xbox One S"),
    ("xbox_series_s", "Xbox Series S"),
    ("xbox_series_x", "Xbox Series X"),
    # PlayStation
    ("ps", "PlayStation"),
    ("ps2", "PlayStation 2"),
    ("ps3", "PlayStation 3"),
    ("ps4", "PlayStation 4"),
    ("ps5", "PlayStation 5"),
    # Nintendo
    ("nintendo_switch", "Nintendo Switch"),
    # Mobile
    ("ios", "iOS"),
    ("android", "Android")
]

game_statuses = [
    ("wishlist", "Wishlist"),
    ("playing", "Currently playing"),
    ("completed", "Completed")
]

game_ratings = [
    (0, " "),
    (1, "\u2606"),
    (2, "\u2606\u2606"),
    (3, "\u2606\u2606\u2606"),
    (4, "\u2606\u2606\u2606\u2606"),
    (5, "\u2606\u2606\u2606\u2606\u2606")
]

class Game(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True)
    platform = models.CharField(max_length=50, choices=game_platforms, null=True)
    status = models.CharField(max_length=50, choices=game_statuses, null=True)
    rating = models.IntegerField(choices=game_ratings, null=True)

    class Meta:
        ordering = ["title"]

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "release_date": self.release_date.isoformat() if self.release_date else None,
            "platform": self.platform,
            "status": self.status,
            "rating": self.rating
        }
