# tildeblog
  *Today I Learned - de blog*

This is a learn-to-use-django project for the [Python Study Central Discord](https://discord.com/invite/6pVFMUEKxX)
In addition to Django, the project is about learning git and practicalities of deployment.

Contributions from any skill level are welcome.  Djanjo newbies are welcome to join
voice discussions.  Coordination, meetups at this [Discord channel](https://discord.com/channels/1200518276023848970/1207695235313049610)

Goal is to create a blog specialized for capturing and presenting "Today I Learned" topics.  Main intent is to create a:
 - "look what I can do" artifact to show an employer, 
 - "look what I did"  to show your manager at review time
 - "stash" technical items you've learned about so you can remind yourself

Here is a sketch of types of features that will appear on landing page:

![image of landing page](https://github.com/regularstuff/tildeblog/sketch-landing-age.png)

## runs on render.com (90 day free trial til April 2024)

This applies to the branch "render"

This repo is set up with render.yaml and render.sh to run on render.com
That host lets you run postgres for 90 days. I don't know of any hosting provider 
that lets you run Django indefinitely for free.  You can probably serially run on AWS free
tier (have to set up a new account every year.)
 
## requirements / spec

 - single author (not a group blog)
 - installable django app
 - article tagging
 - display latex using mathjax or similar
 - flexsearch with live update results (via htmx/alpine.js)
 - has draft queue
 - supports comments and has some spam filter/are you a human challenge
 - quick capture of "seed" from mobile / from discord channel.  So you can remind yourself to write up something you learn
 - "heatmap" similar to github's day/week commit visualization, showing activity over time
 - allow selective feature-by-feature visibility, perhaps by giving a prospective employer a key 

## future (spitballing)

Possible: create a "tildeblog network"  with an engine that discovers collections that seem to
touch on similar topics as yours.  With the idea being you might be interested in "Today I Learned" stuff from people who've
thought it worth mentioning certain things.  This would be most useful if there were a protocol not married to django, as
presumably many people who don't want to run their own django server also learn worthwhile things.



Feel free to sugges features in Github's "Issues" section.
 
## Contributing

If you want to be a collaborator on this, message me (levintennine) in discord.





