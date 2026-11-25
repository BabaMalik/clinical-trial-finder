import unittest

from app import app


class HomePageTests(unittest.TestCase):
    def test_home_page_renders_html(self):
        response = app.test_client().get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "text/html")
        self.assertIn(b"<h1>Clinical Trial Finder</h1>", response.data)


if __name__ == "__main__":
    unittest.main()
