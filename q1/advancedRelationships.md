# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description
The system contains two classes, MusicTrack and Playlist. The musicTrack class represents individual songs with attributes such as title, genre, artist, and block status. The Playlist class contains music tracks and allows multiple tracks to be in the same Playlist
## Inheritance Relationship
Parent: MusicTrack

Child: LikedTrack
Explanation: LikedTrack is a specialized type of MusicTrack. It inherits the general attributes and methods of MusicTrack while adding its own feature for representing a track that has been liked by the user
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation
Explanation: PlayList has a weak has-a relationship with MusicTrack. A Playlist can contain multiple music tracks, but the tracks can still exist independently even if the Playlist is deleted
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
