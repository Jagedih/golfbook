# Golfbook

A simple golf scoring book to store user golf round scores with following features.

- User can create an account.
- User can accept friend requests.
- User can send friend requests.  
- User can add own golf round scores using golf courses found in the database.
- User can add golf rounds to users he is friends with. <p>
- Golf rounds can be either handicap rounds or practise rounds.
- Fairway openings for every hole can be added while giving scores, default is null.
- Putting scores can be added while user inputs scores, default is null.
- GIR can be given while user inputs scores, default is null.  <p>
- User can view leaderboards for every golf course (only handicap rounds included).
- User can view statistics for every course. (played rounds, shot averages from different tee openings)
- User can view his own rounds.
- User can view his own shot averages for every course and hole he has played.
- User can view his own GIR% for every hole he has played.
- User can view his own average putting scores for every hole he has played.  <p>
- Admin can add courses to database.
- Admin can view every round played.
- Admin can delete played golf rounds.
- Admin can delete users and if he does, every round user has played will be deleted from the database.

# Current status:
User can create accounts
User can send friend requests
User can update userprofile
User can post round scores for him/her and friends.
Basic golf course info can be seen from courses.
Admin can add golf courses to the db from the app.

# Not ready:
User can not see his stats from the app. Scores are stored in the db.

# Testing:
You can test current version of the app at https://jagedi-golfbook.herokuapp.com/

Test that you can create valid user accounts.
See that when you add mutual friendships, you can see the friend from the profile.
Test that you can add golf scores to you and your friends.
Test that all the pages render.
