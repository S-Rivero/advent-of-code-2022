const fs = require("fs");

console.log('Processing')

for (i = 0; i < 31; i++) {
    
    path = __dirname + '/node.js//Day ' + (i+1) + '/';
    //let path = __dirname + '/node.js/Day 1/';
    if (!fs.existsSync(path)){
        fs.mkdirSync(path);
        
        for( z = 1; z < 3; z++){
            fs.writeFileSync(
                path + 'exercise_'+z+'.txt',
                `Here you should paste the exercise 'your puzzle input'`
            );

            fs.writeFileSync(
                path + 'exercise_'+z+'.js',
                "// Here you can code the solution"
            );
        }
    }  else {
        console.log('Debe borrar las carpetas existentes en "node.js"');
        return false;
    }

}
    
console.log('Operation Finished')