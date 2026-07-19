import unittest

from build import extract_domains


class ExtractDomainsTest(unittest.TestCase):
    def test_extracts_unique_domains_from_hosts(self):
        source = [
            "# comment",
            "0.0.0.0 Ads.Example.com ads.example.com.",
            "127.0.0.1 localhost",
            "::  tracker.example.net",
            "0.0.0.0 10.0.0.1",
            "not-an-ip ignored.example",
        ]

        self.assertEqual(
            extract_domains(source),
            ["ads.example.com", "tracker.example.net"],
        )


if __name__ == "__main__":
    unittest.main()
