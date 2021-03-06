# -*- coding: utf-8 -*-

import six

from wargaming import settings
from wargaming.api import BaseAPI, MetaAPI
from wargaming.games.wot.accounts import Accounts
from wargaming.games.wot.auth import Auth
from wargaming.games.wot.clans import Clans
from wargaming.games.wot.globalwar import GlobalWar
from wargaming.games.wot.encyclopedia import Encyclopedia
from wargaming.games.wot.ratings import Ratings
from wargaming.games.wot.clan_ratings import ClanRatings
from wargaming.games.wot.tanks import Tanks

__all__ = ('API', )


@six.add_metaclass(MetaAPI)
class API(BaseAPI):
    """World of Tanks API client"""

    def __init__(self, application_id, language=settings.DEFAULT_LANGUAGE):
        """
        :param application_id: Your application ID from the https://wargaming.net/developers/applications/
        :type application_id: str
        :param language: Language for the requests (defaults to English)
        :type language: str
        """

        super(API, self).__init__(application_id, language,
                                  base_url='https://api.worldoftanks.com/wot/')

    accounts = Accounts()

    auth = Auth()

    clans = Clans()

    globalwar = GlobalWar()

    encyclopedia = Encyclopedia()

    ratings = Ratings()

    clan_ratings = ClanRatings()

    tanks = Tanks()
