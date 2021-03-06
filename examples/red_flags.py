from __future__ import print_function
import config

config.setup_examples()
import infermedica_api


if __name__ == '__main__':
    api = infermedica_api.get_api()

    # Prepare diagnosis request it need to have sufficient amount of evidences
    # The most appropriate way to get a request way for red_flags method is to
    # use the one which has been created while interacting with diagnosis.
    # For the example purpose a new one is created.
    request = infermedica_api.Diagnosis(sex='female', age=35)

    request.add_symptom('s_10', 'present')
    request.add_symptom('s_608', 'present')

    # call the red_flags method
    request = api.red_flags(request)

    # and see the results
    print('\n\n', request)
