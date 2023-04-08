from ..base import BaseHandlers


class ProjectsHandlers(BaseHandlers):
    def create_new_project_v1(self, title: str, code: str, description: str = None):
        handler = "v1/project"
        json = {
            "title": title,
            "code": code,
            "description": description
        }
        return self.client.post(handler, json)

    def get_project_by_code_v1(self, code: str):
        handler = f"v1/project/{code}"
        return self.client.get(handler)

    def get_all_projects_v1(self):
        handler = "v1/project"
        return self.client.get(handler)
