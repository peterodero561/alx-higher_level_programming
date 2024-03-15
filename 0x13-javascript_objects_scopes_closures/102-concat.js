#!/usr/bin/node
const fs = require('fs');

function concatFiles(file1Path, file2Path, destinationPath) {
    try {
        // Read the content of the first file
        const data1 = fs.readFileSync(file1Path, 'utf8');
        
        // Read the content of the second file
        const data2 = fs.readFileSync(file2Path, 'utf8');
        
        // Concatenate the contents of both files
        const concatenatedData = data1 + data2;
        
        // Write the concatenated data to the destination file
        fs.writeFileSync(destinationPath, concatenatedData);
        
        console.log("Files concatenated successfully!");
    } catch (err) {
        console.error("An error occurred:", err);
    }
}

// Check if arguments are provided
if (process.argv.length !== 5) {
    console.error("Usage: node script.js <file1Path> <file2Path> <destinationPath>");
    process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

concatFiles(file1Path, file2Path, destinationPath);
