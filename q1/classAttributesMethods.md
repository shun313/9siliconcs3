# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
Describe any changes made to your original class.
- I changed the Like concept to isBlocked which shows whether you blocked a specific artist.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |

|---|---|---|---|
| Title | String | Public | Essential identifier that can be easily searched |
| Genre | String | Public | Information used to recommend songs matching the users preferences | 
| Artist | String | Public | The artist's name can be viewed to know who created it |
| isBlocked | Boolean | Private | To prevent tampering and keep privacy, user's status remains protected |

## Updated UML Class Diagram

![Class Diagram](images/classDiagramSG5.png)

## Python Implementation

[View Python Source](classImplementation.py)

## Test Run

![Test Run](images/classTestRun.png)

## Object Diagram

![Object Diagram](images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?

### Which method changes the state of your object?

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?
