# Class Relationships: Association and Multiplicity 
## Previous Work 
[Part I - Classes and Objects](classObjectUML.md) 
[Part II - Class Attributes and Methods](classAttributesMethods.md) 
## Existing Class 
Class: MusicTrack
Description: A MusicTrack represents a song in a music library or playlist.
## New Related Class 
Class: Playlist
Description: A playlist represents a storage, it includes songs the user has added in that specific playlist
## Association 
Relationship: Playlist contains MusicTrack
Explanation: A playlist can contain multiple MusicTracks objects.
## Multiplicity
Multiplicity: 0..*
Explanation: 
## UML Class Relationship Diagram 
![Class Relationship Diagram](images/classRelationshipDiagram.png) 
## Python Implementation 
[View Python Source](classRelationships.py) 
## Test Run 
![Relationship Test Run](images/relationshipTestRun.png) 
## Object Relationship Diagram 
![Object Relationship Diagram](images/objectRelationshipDiagram.png) 
## Analysis 
### What is the association between your two classes? 

### What multiplicity did you choose and why? 

### How did you implement the relationship in Python? 

### Why did you store an object reference instead of copying its data? 

### If your relationship uses many, why is a list appropriate? 

