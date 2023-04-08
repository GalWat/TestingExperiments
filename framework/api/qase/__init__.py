from framework.api.base import BaseApi
from config.config import settings
from .projects import ProjectsHandlers


class QaseApi(BaseApi):
    def __init__(self):
        super(BaseApi, self).__init__(service_url=settings.qase.api.url)
        self.global_headers = {
            "Token": settings.qase.api.token
        }

        self.projects = ProjectsHandlers(self)
