site_history = [] #Empty set to hold the sites that have been visited
def new_site(site):
    site_history.append(site) #Add the new site to the history

def prev_site():
    site_history.pop() #Remove the most recent site from the history

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