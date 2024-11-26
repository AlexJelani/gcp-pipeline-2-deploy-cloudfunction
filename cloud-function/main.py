import functions_framework

@functions_framework.http
def function_1_v10(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'V1.0 with CI/CD'
    return 'function {}!'.format(name)

