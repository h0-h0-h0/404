# HTTP response status codes
# 404

# for pytest
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    
print('404 Not Found')
print('')
print('''404 Not Found
The HTTP 404 Not Found response status code indicates that the server cannot
find the requested resource. Links that lead to a 404 page are often called
broken or dead links and can be subject to link rot.

A 404 status code only indicates that the resource is missing: not whether
the absence is temporary or permanent. If a resource is permanently removed,
use the 410 (Gone) status instead.''')

