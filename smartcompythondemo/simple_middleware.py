def simple_middleware(get_response):

  def middleware(request):
      # forward moving area
      print("This is before view")
      response = get_response(request)
      print("This is after view")
      # backward moving area
      return response

  return middleware


def another_middleware(get_response):

  def anothermiddleware(request):
      # forward moving area
      print("This is before another view")
      response = get_response(request)
      print("This is after another view")
      # backward moving area
      return response

  return anothermiddleware



# passing a function as parameter
# response = get_response()
# return response
# def sum(a,b):
#     return a+b
#
# def divide(a, b):
#     return a/b
#
# def perform_op(op, a, b):
#     return op(a,b)
#
# # perform_op(sum, 2, 3)
# perform_op(divide, 2, 3)