"""Factories for the TrackArtistLocalizedMetadata model."""

import factory

from python_crud.models.vectorapi_users import VectorapiUsers


class VectorapiUsersFactory(factory.Factory):
    """Factory to create VectorapiUsers models for testing."""

    class Meta:
        """Meta definition for the factory."""
        model = VectorapiUsers

    user_id = factory.Sequence(lambda n: 100 + n)
    name = factory.Sequence(lambda n: 'User {}'.format(n))
    api_key = factory.Sequence(lambda n: n)
    api_secret = factory.Sequence(lambda n: 'Secret {}'.format(n))
