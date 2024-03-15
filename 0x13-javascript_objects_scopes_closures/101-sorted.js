#!/usr/bin/node
const { occurrencesByUserId } = require('./101-data');

function computeUserIdsByOccurrence(occurrencesDict) {
    const userIdsByOccurrence = {};
    
    // Iterate through the occurrences dictionary
    for (const userId in occurrencesDict) {
        const occurrence = occurrencesDict[userId];
        
        // If the occurrence is not already a key in the new dictionary, create it
        if (!userIdsByOccurrence[occurrence]) {
            userIdsByOccurrence[occurrence] = [userId];
        } else {
            // If the occurrence is already a key, append the user id to the existing list
            userIdsByOccurrence[occurrence].push(userId);
        }
    }
    
    return userIdsByOccurrence;
}

// Compute the dictionary of user ids by occurrence
const userIdsByOccurrence = computeUserIdsByOccurrence(occurrencesByUserId);

// Print the new dictionary
console.log(userIdsByOccurrence);
