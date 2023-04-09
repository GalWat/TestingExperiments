from framework.api.base import BaseApi
from config.config import settings
from .projects import ProjectsHandlers


class QaseApi(BaseApi):
    def __init__(self):
        super().__init__(service_url=settings.qase.api.base_url)
        self.global_headers = {
            "Token": settings.qase.api.token
        }

        self.projects = ProjectsHandlers(self)
