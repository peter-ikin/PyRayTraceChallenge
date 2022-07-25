from behave import *
from raytracer.tuples import *

use_step_matcher("re")


@given("a <- tuple\(4\.3, -4\.2, 3\.1, 1\.0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = Point(4.3, -4.2, 3.1)


@then("a\.x = 4\.3")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    test_tuple = context.response
    assert(test_tuple.x == 4.3)


@step("a\.y = -4\.2")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    test_tuple = context.response
    assert(test_tuple.y == -4.2)


@step("a\.z = 3\.1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    test_tuple = context.response
    assert(test_tuple.z == 3.1)


@step("a\.w = 1\.0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    test_tuple = context.response
    assert(test_tuple.w == 1.0)


@step("a is a point")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(isinstance(context.response, Tuple))
    assert(type(context.response) is Point)


@step("a is not a vector")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(isinstance(context.response, Tuple))
    assert(type(context.response) is not Vector)


@given("a <- tuple\(4\.3, -4\.2, 3\.1, 0\.0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = Vector(4.3, -4.2, 3.1)


@step("a\.w = 0\.0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    test_tuple = context.response
    assert(test_tuple.w == 0.0)


@step("a is not a point")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(isinstance(context.response, Tuple))
    assert(type(context.response) is not Point)


@step("a is a vector")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert(isinstance(context.response, Tuple))
    assert(type(context.response) is Vector)


@given("p <- point\(4, -4, 3\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = Point(4, -4, 3)


@then("p = tuple\(4, -4, 3, 1\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    t = Tuple(4, -4, 3, 1)
    assert(context.response == t)


@given("v <- vector\(4, -4, 3\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = Vector(4, -4, 3)


@then("v = tuple\(4, -4, 3, 0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    t = Tuple(4, -4, 3, 0)
    assert(context.response == t)


@given("a1 <- tuple\(3, -2, 5, 1\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.a1 = Tuple(3, -2, 5, 1)


@step("a2 <- tuple\(-2, 3, 1, 0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.a2 = Tuple(-2, 3, 1, 0)


@then("a1 \+ a2 = tuple\(1, 1, 6, 1\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.a1 + context.a2
    expected = Tuple(1, 1, 6, 1)
    assert(result == expected)


@given("p1 <- point\(3, 2, 1\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.p1 = Point(3, 2, 1)


@step("p2 <- point\(5, 6, 7\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.p2 = Point(5, 6, 7)


@then("p1 - p2 = vector\(-2, -4, -6\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.p1 - context.p2
    expected = Vector(-2, -4, -6)
    assert(result == expected)


@given("p <- point\(3, 2, 1\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.p = Point(3, 2, 1)


@step("v <- vector\(5, 6, 7\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v = Vector(5, 6, 7)


@then("p - v = point\(-2, -4, -6\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.p - context.v
    expected = Point(-2, -4, -6)
    assert(result == expected)


@given("v1 <- vector\(3, 2, 1\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v1 = Vector(3, 2, 1)


@step("v2 <- vector\(5, 6, 7\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v2 = Vector(5, 6, 7)


@then("v1 - v2 = vector\(-2, -4, -6\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.v1 - context.v2
    expected = Vector(-2, -4, -6)
    assert(result == expected)


@given("zero <- vector\(0, 0, 0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.zero = Vector(0, 0, 0)


@step("v <- vector\(1, -2, 3\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v = Vector(1, -2, 3)


@then("zero - v = vector\(-1, 2, -3\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.zero - context.v
    expected = Vector(-1, 2, -3)
    assert(result == expected)


@given("a <- tuple\(1, -2, 3, -4\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.a = Tuple(1, -2, 3, -4)


@then("-a = tuple\(-1, 2, -3, 4\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = -context.a
    expected = Tuple(-1, 2, -3, 4)
    assert(result == expected)


@then("a \* 3\.5 = tuple\(3\.5, -7, 10\.5, -14\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.a * 3.5
    expected = Tuple(3.5, -7, 10.5, -14)
    assert(result == expected)

@then("3\.5 \* a = tuple\(3\.5, -7, 10\.5, -14\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = 3.5 * context.a
    expected = Tuple(3.5, -7, 10.5, -14)
    assert(result == expected)

@then("a \* 0\.5 = tuple\(0\.5, -1, 1\.5, -2\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.a * 0.5
    expected = Tuple(0.5, -1, 1.5, -2)
    assert(result == expected)


@then("a / 2 = tuple\(0\.5, -1, 1\.5, -2\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.a / 2
    expected = Tuple(0.5, -1, 1.5, -2)
    assert(result == expected)


@given("v <- vector\(1, 0, 0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v = Vector(1, 0, 0)


@then("magnitude\(v\) = 1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.v.magnitude()
    expected = 1
    assert (result == expected)


@given("v <- vector\(0, 1, 0\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v = Vector(0, 1, 0)


@given("v <- vector\(0, 0, 1\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v = Vector(0, 0, 1)


@given("v <- vector\(1, 2, 3\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v = Vector(1, 2, 3)


@then("magnitude\(v\) = √14")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    result = context.v.magnitude()
    expected = math.sqrt(14)
    assert (result == expected)


@given("v <- vector\(-1, -2, -3\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.v = Vector(-1, -2, -3)
