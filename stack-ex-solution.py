site_history = []
def new_site(site):
    site_history.append(site)

def prev_site():
    site_history.pop()

'''
Test cases
'''
new_site('my.byui.edu')
new_site('byui.instructure.com')
new_site('twitter.com')
print(site_history)
prev_site()
print(site_history)
new_site('youtube.com')
new_site('iplan.byui.edu')
print(site_history)
prev_site()
prev_site()
print(site_history)