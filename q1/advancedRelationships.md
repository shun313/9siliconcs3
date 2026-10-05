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

1. Why did you choose your inheritance relationship?
- I chose MusicTrack as the parent class and LikedTrack as the child class because a liked track is stikl a type of music track. LikedTrack needs the same basic information and functions as MusicTrack. This makes inheritance appropriate because the child class is a more specific version of the parents class.

2. How did inheritance reduce duplicate code?
- Inheritance allowed LikedTrack to reuse the attributes and methods already written in MusicTrack. Instead of rewriting properties such as title, genre, and artist, the child class can inherit them from the parent. The methods such as play() and shiwLyrics() can also be reused

3. Why is your HAS-A relationship Composition or Aggregation?
- The relationship between Playlist and MusicTrack is aggregation because a playlist contains music tracks that can exist independently. If a playlist is deleted, the music tracks do not have to be deleted. The tracks can also be placed in other playlists.

4. What is the difference between Association from Part III and the advanced relationship you implemented?
- Association simply shows that two classes are connected or interact with each other. Aggregation is more specific because it shows that one class contains another object while allowing the contained object to exist independently. Inheritance is also different because it represents an IS-A relationship between a parent and child class.

5. How does your design follow the DRY principle?
- The design follows the DRY principle by avoiding repeated code between MusicTrack and LikedTrack. The child class inherits common attributes and methods from MusicTrack instead of rewriting them. This makes the code shorter, easier to maintain, and less repetitive.
