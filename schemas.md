## Song

Schema for a song. No name, artist, anything, just the uuid and the link to where the file is hosted. All of that is in the metadata object keyed by the uuid.

```JSON
{
    "type": "object",
    "properties": {
        "song_uuid": {
            "type": "string",
            "format": "uuid"
        },
        "stream_link": {
            "type": "string",
            "format": "url"
        },
        "metadata": {
            "$ref": "#/components/schemas/Metadata"
        }
    }
}
```

## Playlist

A playlist comprises any collection of songs, whether that be an album, EP, playlist, etc.

```JSON
{
    "type": "object",
    "properties": {
        "plist_uuid": {
            "type": "string",
            "format": "uuid"
        },
        "songs": {
            "type": "array",
            "items": {
                "plist_track": {
                    "number": {
                        "type": "int"
                    },
                    "artist": {
                        "$ref": "#/components/schemas/Artist"
                    },
                    "metadata": {
                        "$ref": "#/components/schemas/Metadata" 
                    },
                    "song": {
                        "$ref": "#/components/schemas/Song"
                    }
                }
            }
        }
    }
}
```

## Artist

Object containing data about an artist.

```JSON
{
    "type": "object",
    "properties": {
        "artist_uuid": {
            "type": "string",
            "format": "uuid"
        },
        "metadata": {
            "$ref": "#/components/schemas/Metadata"
        }
    }
}
```

## Metadata

Miscillaneous object that holds contextual data for other objects. Eg album artwork, liner notes, artist bio, etc. Field schema not enforced beyond unique identifier.

```JSON
{
    "type": "object",
    "properties": {
        "mdata_uuid": {
            "type": "string",
            "format": "uuid"
        }
    }
}
```
