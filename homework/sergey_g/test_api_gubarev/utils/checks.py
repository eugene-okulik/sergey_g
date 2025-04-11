from endpoints.endpoint import Endpoint
import allure


class Checks(Endpoint):

    @allure.step('Check that title is the same as sent')
    def check_response_title_is_correct(self, title):
        assert self.json['title'] == title, 'title is not title'

    @allure.step('Check that title is the same as sent')
    def check_response_message_after_delete(self, object_id):
        print(self.response)
        assert self.response.json()['message'] == f'Object with id = {object_id} has been deleted.'

    @allure.step('Check that response is 200')
    def check_that_response_is_200(self):
        assert self.response.status_code == 200, '200 is not 200'

    @allure.step('Check that 400 error received')
    def check_bad_requiest_is_400(self):
        assert self.response.status_code == 400, '400 is not 400'

    @allure.step('Check that 404 error received')
    def check_bad_requiest_is_404(self):
        assert self.response.status_code == 404, '400 is not 400'

    @allure.step('Check that title is the same as sent')
    def check_id_in_response(self):
        assert 'id' in self.response.json(), 'Check for the id in the response'
