# coding: utf8
from atlassian import Confluence

confluence = Confluence(
    url='http://localhost:8090',
    username='admin',
    password='admin')

status = confluence.update_page(
    page_id=123456,
    title='This is the new title',
    body='This is the new body')

print(status)
