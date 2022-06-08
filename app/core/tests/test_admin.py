"""
Tests for Django admin modofications
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSetupTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create User and Client"""

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='parola1234',
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='parola1234',
            name='Test User',
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        url = reverse('admin:core_user_changelist')
        page = self.client.get(url)

        self.assertContains(page, self.user.email)
        self.assertContains(page, self.user.name)

    def test_user_change_page(self):
        """Test user change page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        page = self.client.get(url)

        self.assertEqual(page.status_code, 200)
