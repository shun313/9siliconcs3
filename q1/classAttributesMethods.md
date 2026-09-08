# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
Describe any changes made to your original class.
- I changed the Like concept to isBlocked which shows whether you blocked a specific artist.
- I changed the addToLikedSongs() method to getBlocked() which is the option to block artists.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Title | String | Public | Essential identifier that can be easily searched |
| Genre | String | Public | Information used to recommend songs matching the users preferences | 
| Artist | String | Public | The artist's name can be viewed to know who created it |
| isBlocked | Boolean | Private | To prevent tampering and keep privacy, user's status remains protected |

## Updated UML Class Diagram

<img width="720" height="717" alt="image" src="https://github.com/user-attachments/assets/64344b27-4b6a-4b76-866e-1d99c6ed792e" />

## Python Implementation



## Test Run

<img width="679" height="229" alt="image" src="https://github.com/user-attachments/assets/5087256d-bf01-4728-bf5d-9ee3a0a0cba5" />

## Object Diagram

<img width="881" height="885" alt="image" src="https://github.com/user-attachments/assets/c327110a-f593-45b4-a00d-57ba32455651" />

## Analysis

### Why did you make your chosen attribute private?
It prevents tampering and keeps the user's privacy hidden. It also keeps the program organized and protected.

### Which method changes the state of your object?
The blockArtist() method changes the object's state by changing the blocked status from False to True.

### How did your two objects demonstrate that instances are independent?
Changing Object 1's blocked status did not affect Object 2. Object 1 became True, while Object 2 stayed False.

### What is the difference between your class diagram and your object diagram?
The class diagram shows the blueprint of the MusicTrack class. The object diagram shows the actual values of the two objects created from that class.
