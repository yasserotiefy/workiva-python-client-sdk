# coding: utf-8

"""
    Platform API

    Use the Workiva Platform API to programmatically manage items in the Workiva platform, such as files, folders, tasks, comments, documents, spreadsheets, and presentations. 

    The version of the OpenAPI document: v1
    Contact: platformsupport@workiva.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.task import Task

class TestTask(unittest.TestCase):
    """Task unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Task:
        """Test Task
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Task`
        """
        model = Task()
        if include_optional:
            return Task(
                id = '128f274395254cf17eda6b3eb3d021b9',
                title = 'Review Document',
                description = '',
                status = 'Created',
                due_date = '2019-10-30T00:00Z',
                source_url = 'https://app.wdesk.com/tasks/d/UVdOauIzVaVkQjdxTmzNNUOEUTQOakEnTnpJTE9ENXkuEkdGeaF4OENNJEV3NUTBmA?token=NTc0NDU2MTg1MjM0ODUyTM',
                assignee = openapi_client.models.user.User(
                    id = 'V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD', 
                    user_name = '', 
                    display_name = '', 
                    first_name = '', 
                    last_name = '', 
                    email = '', ),
                created = openapi_client.models.action.Action(
                    user = openapi_client.models.user.User(
                        id = 'V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD', 
                        user_name = '', 
                        display_name = '', 
                        first_name = '', 
                        last_name = '', 
                        email = '', ), 
                    date_time = '2019-10-30T15:03:27Z', ),
                modified = openapi_client.models.action.Action(
                    user = openapi_client.models.user.User(
                        id = 'V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD', 
                        user_name = '', 
                        display_name = '', 
                        first_name = '', 
                        last_name = '', 
                        email = '', ), 
                    date_time = '2019-10-30T15:03:27Z', ),
                completed = openapi_client.models.action.Action(
                    user = openapi_client.models.user.User(
                        id = 'V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD', 
                        user_name = '', 
                        display_name = '', 
                        first_name = '', 
                        last_name = '', 
                        email = '', ), 
                    date_time = '2019-10-30T15:03:27Z', ),
                location = openapi_client.models.task_location.TaskLocation(
                    file = '124efa2a142f472ba1ceab34ed18915f', 
                    file_segment = '465ttdh2a142y75ehsft5ab34edf5675', )
            )
        else:
            return Task(
        )
        """

    def testTask(self):
        """Test Task"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()