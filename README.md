# How to dirty get started with Travis CI, with Python, on Github.
Short Travis getting started with python, quick and dirty.[![Build Status](https://travis-ci.com/gianfa/tutorials-travis_testing_python.svg?branch=master)](https://travis-ci.com/gianfa/tutorials-travis_testing_python)

A lot of tutorials are available about this topic, so I will give you only the fundamentals to **effectively** setup your first **COMPLETE** travis build pass with python.

### Before to start ###
Before to start with this tutorial you should know that **you will need to make code *tests* by yourself in order to use Travis**. If you don't know what *tests* are, than you better read a little bit about it at the end of this tutorial. Anyway Keep Calm and Carry on, you will make your first build pass at the end of this.

### How-to step by step ###

#### 1. Setup Github repository ####
1.  Create a new Github repository into your profile, say *tutorials-travis_testing_python*.<br>Now you should have a branch YOURNAME/tutorials-travis_testing_python/.
<br>( compare with this repository )
2.  Create a new python module, say *test_testami.py* (❗️ it must be named with a prefix **test_**) and write into it:
   *   a python function *funzione*
   *   ❗️ a *pytest* (python testing framework) function *test_funzione* that will assert the output of *funzione*
<br>( compare with *test_testami.py* in this repository )
3. Create the *.travis.yml* file containing the configuration about Travis behaviour.
<br>( compare with *.test.yml* in this repository )
4. Create a *requirements.txt* file with the required modules for your module to run. If it needs no other modules let it empty, but create it anyway.

#### 2. Setup Travis CI ####
2.  Go to [Travis CI](https://travis-ci.com/)
2.  Sign Up or Sign In with your Github account
2.  From you Travis console, reachable at https://travis-ci.com/profile/**YOURGITHUBNAME**,  click on *Manage Repositories on Github* and access with your Github password. Now you should be in your Travis CI Github Manager and you should be able to see in particular two sections: *Permissions* and *Repository access*.
2.  Go to *Repository access* and make your choice. I prefer to **_Select Repositories_**, specifying *tutorials-travis_testing_python*.
2.  Select *Approve and Install*. Now on, Travis will launch a build at every commit you will do to your repository. 
2.  Yes, everyone, automatically.
2.  Go back to your Travis CI console and select **_Sync account_**.
2.  From your Travis CI console you should see under *Repositories* tab the name of the repository you just added, *tutorials-travis_testing_python*, so click on it to go to the Travis CI branch related to it. From there you can see the builds.

#### 3. Do your first commit and build ####
3.  Go to your Github repository and commit whatever you want. For example you can edit your readme.
3.  Jump to your Travis CI branch and watch it working. If you followed everything well you should see the beautiful exit line<br>
```bash
     =========================== 1 passed in 0.02 seconds ===========================

     The command "pytest" exited with 0.
     
     Done. Your build exited with 0.
```
3.  Read again 2.6

#### 4. Hum, so everything will pass?? ####
1.  Go editing your *test_testami.py* file changing the returned value in a wrong way, for instance concatenating a *str* with a *int* and see what happens

#### 5. Grand Finale ####
1.  Add your Travis CI Passing Badge to your README.md! You can do it reading this easy guide: https://docs.travis-ci.com/user/status-images/.
<br> ...or you can just add
``` [![Build Status](https://travis-ci.com/YOURGITHUBNAME/travis_testing_python.svg?branch=master)](https://travis-ci.com/YOURGITHUBNAME/travis_testing_python)``` but maybe it will not be enough... (I warmly suggest you to read the guide, it's only 2 steps!).

#### Et voilà! ####
Tests are done. Enjoy your brand new badge [![Build Status](https://travis-ci.com/gianfa/tutorials-travis_testing_python.svg?branch=master)](https://travis-ci.com/gianfa/tutorials-travis_testing_python)
<br>
BTW... you can fork this repository and make it run instantly after connected with your Travis CI 

