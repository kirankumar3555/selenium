#robotic framework is a generic test automation framework for acceptance testing.
#It is a Acceptance test driven development framework
#It utilizes keyword driven testing approach
#provides test libraries implemented either in python or java and we
# can also create new keywords from existing ones with the same syntax
# end user can test this using keywords so no programming language knowledge is required
# to know this framework
# robotic framework has 4 libraries inside it.
# they are builtin library,selenium library,db library, etc.
# we need to import these libraries while performing testing in frameworks.
# these frameworks have keywords which are indeed connected to the selenium methods
# for example if we have a keyword open browser in robotic framework, it is
# connected to selenium code webdriver.chrome(service=s)  and when we use this keyword
# the browser gets opened because it internally uses the selenium code
# we need to install roboticframework,roboticframework-selenium libraries
# we need to add intellibot package into our pycharm because our robotic testcases files end
# with .robot file our pycharm won't be able to recognise them so we need to install intellibot plugin
# intellibot@seleniumlibrary patch should be installed as a plugin
# this intellibot also gives autosuggestions for the keywords in the roboticframework.
