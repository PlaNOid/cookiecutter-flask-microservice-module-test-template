from app.{{cookiecutter.module_name}}s.models import {{cookiecutter.module_name|capitalize}}


def test_create_{{cookiecutter.module_name|lower}}(client):
    resp = client.post(
        endpoint='{{cookiecutter.module_name|lower}}s.add_{{cookiecutter.module_name|lower}}_view',
    )

    assert 'data' in resp
    data = resp['data']

    assert 'id' in data
    assert {{cookiecutter.module_name|capitalize}}.query.filter_by(id=data['id']).one_or_none()


def test_{{cookiecutter.module_name|lower}}_list(client):
    resp = client.get(
        endpoint='{{cookiecutter.module_name|lower}}s.list_view',
    )

    assert 'data' in resp
    data = resp['data']

    assert 'results' in data
    assert 'total' in data


def test_{{cookiecutter.module_name|lower}}_by_id(client):
    resp = client.get(
        endpoint='{{cookiecutter.module_name|lower}}s.{{cookiecutter.module_name|lower}}_by_id_view',
        {{cookiecutter.module_name|lower}}_id={{cookiecutter.module_name|capitalize}}.query.first().id,
    )

    assert 'data' in resp
    data = resp['data']

    assert 'id' in data


def test_update_{{cookiecutter.module_name|lower}}(client):
    resp = client.put(
        endpoint='{{cookiecutter.module_name|lower}}s.update_{{cookiecutter.module_name|lower}}_view',
        {{cookiecutter.module_name|lower}}_id={{cookiecutter.module_name|capitalize}}.query.first().id,
    )

    assert 'data' in resp
    data = resp['data']

    assert 'id' in data
    assert {{cookiecutter.module_name|capitalize}}.query.filter_by(id=data['id']).one().to_dict() == data


def test_delete_{{cookiecutter.module_name|lower}}(client):
    resp = client.delete(
        endpoint='{{cookiecutter.module_name|lower}}s.delete_{{cookiecutter.module_name|lower}}_view',
        {{cookiecutter.module_name|lower}}_id={{cookiecutter.module_name|capitalize}}.query.first().id,
    )

    assert 'data' in resp
    data = resp['data']

    assert not {{cookiecutter.module_name|capitalize}}.query.filter_by(id=data['id']).one_or_none()
