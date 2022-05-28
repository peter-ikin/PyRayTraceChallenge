from behave import *

use_step_matcher("re")


@given("a <- tuple\(4\.3, -4\.2, 3\.1, 1\.0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given a <- tuple(4.3, -4.2, 3.1, 1.0)')


@then("a\.x = 4\.3")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then a.x = 4.3')


@step("a\.y = -4\.2")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a.y = -4.2')


@step("a\.z = 3\.1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a.z = 3.1')


@step("a\.w = 1\.0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a.w = 1.0')


@step("a is a point")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a is a point')


@step("a is not a vector")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a is not a vector')