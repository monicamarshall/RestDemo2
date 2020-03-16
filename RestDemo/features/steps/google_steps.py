import behave


@behave.when('we visit google')
def step_when(context):
    context.browser.get('http://www.google.com')

@behave.then('it should have a title "Google"')
def step_then(context):
    assert context.browser.title == "Google"
