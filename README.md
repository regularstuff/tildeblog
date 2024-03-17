# tildeblog

  *Today I Learned - de blog*

Updated: March 16 2024

[4 min Video with new features]()

This is a learn-to-use-django project. Goal is to create a blog specialized for capturing and presenting
"Today I Learned" topics (more detail below). Contributions from any skill level are welcome. The open issues are
listed in github in the usual place.

In addition to Django, the project is about learning to collaborate in github, and we will help new
contributors get started with git.

[New to Django?](#if-you-are-new-to-django) | [New to Github Collaboration/PRs?](#if-you-are-new-to-github) | [New to Git?](#if-you-are-new-to-git)  | [New to Python?](#if-you-are-new-to-python)

Discussion is on the [Python Study Central Discord Server](https://discord.com/invite/6pVFMUEKxX) (that is
the invite link.)  The conversation is in channel "tildablog-dev". We try to have occasional voice meetings.

| [How to run on local](#running-on-local) | [Project Goals](#project-goals) |

You can see tildeblog running on Render, and can add stuff to it. The styling is **very** rough as of March 16. Render
"spins down" free-plan websites if they aren't accessed frequently, so it is likely to take a minute or so
to come up if you look at it.   It is at https://tildeblog.onrender.com.

## Project Goals
Goal is to create a blog specialized for capturing and presenting "Today I Learned" topics.  Main intent is to create a:
 - "look what I can do" artifact to show an employer 
 - "look what I did"  to show your manager at review time
 - "stash" technical items you've learned about so you can remind yourself

Here is a sketch of types of features that will appear on landing page:

![image of landing page](https://github.com/regularstuff/tildeblog/blob/main/sketch-landing-page.png)

## Running on local

*Help wanted - newbie friendly video walkthru for specific IDE/linux/windows/mac.  See [issue 7](https://github.com/regularstuff/tildeblog/issues/7)*


- Clone the project
- Create and activate virtual environment if your IDE does not do that for you
- Install requirements if your IDE doesn't do it for you (at the shell, run `pip install -r requirements.txt`)
- Set an environment variable, DJANGO_SETTINGS_MODULE.  Set it to "django_root.laptop_settings".
  - This project deliberately ships "not ready to use" with respect to that Environment Variable, see issue 6 on github.  If you don't want to bother with environment variable you can change code in manage.py to load "django_root.laptop_settings.py"
- run `manage.py migrate`
- run `manage.py runserver`

You should now be able to browse to it at http://localhost:8000


## runs on render.com (90 day free trial til April 2024)

This applies to the branch "render"

This repo is set up with render.yaml and render.sh to run on render.com
That host lets you run postgres for 90 days. I don't know of any hosting provider 
that lets you run Django indefinitely for free.  You can probably serially run on AWS free
tier (have to set up a new account every year.)
 

 
## Contributing

If you want to be a collaborator on this, message me (levintennine) in discord. And you can contribute also
by suggesting features in Github's "Issues" section.

### If you are new to Django

Tbd, let's talk about what is useful here

### If you are new to Github

Pull requests are confusing and that is the main way to collaborate.  [More, looking for inputon what to put here]

### If you are new to Git

You have to know a bit about git to work with other software developers in the 2020s.  If you are reading sourcecode
on the github website, or if you are using "zip" to get repositories, you have to learn how to clone, commit and 
push before you can work productively with others.  We can help you, but there is a good amount of study, too.

### If you are new to Python

Uh-oh.  Depending on your learning style, jumping in with Django is likely to be a little bewildering.  Besides 
using a lot of common python programing, Django involves a lot of what seems like "magic".  It is a 20 year old framework that
has evolved a few patterns that are practically domain-specific-languages.  You're welcome to contribute and
learn with us.  If you find it overwhelming though, remember a lot of the detail is Django-specific, it *doesn't*
mean python is too hard for you.

