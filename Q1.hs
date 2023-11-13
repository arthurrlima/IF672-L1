push :: [Int] -> Int -> [Int]
push pilha x = pilha ++ [x]

top :: [Int] -> Int
top [x]     = x
top (x:xs)  = top xs

pop :: [Int] -> [Int]
pop [] = error "Pilha Vazia"
pop (x:xs) 
 | (x == (top (x:xs)))      = xs
 | otherwise                = x:(pop xs)

is_empty :: [Int] -> Bool
is_empty []     = True
is_empty _      = False

checkParidade :: Int -> Int -> Bool
checkParidade x y 
 | x `mod` 2 == y `mod` 2   = True
 | otherwise                = False

doSubtracao :: Int -> Int -> Int
doSubtracao x y 
 | x >= y       = x-y
 | otherwise    = y-x

novaJogada :: Int -> [Int] -> [Int]
novaJogada n pilha
 | pilha == []                        = push pilha n
 | checkParidade (top pilha) n        = novaJogada (doSubtracao (top pilha) n) (pop pilha)
 | otherwise                          = push pilha n

readAndPrintLines :: IO ()
readAndPrintLines = do
    putStrLn "Enter moves (enter 0 to finish):"
    readLines []

readLines :: [String] -> IO ()
readLines linesSoFar = do
    line <- getLine
    if line == "0"
        then printLines linesSoFar
        else readLines (linesSoFar ++ [line])

printLines :: [String] -> IO ()
printLines linesToPrint = do
    putStrLn "You entered the following lines:"
    print linesToPrint


{-gameControl :: IO ()
gameControl = do
    line <- getInt
    if line > 0 then
        novaJogada line []
    else
        return()


readMove :: Int -> [Int] -> IO () -> [Int]
readMove n = do
    move <- getInt
    if move == 0 then
        novaJogada move []
    else
       return []
-}
    

getInt :: IO Int
getInt = read <$> getLine

main :: IO ()
main = readAndPrintLines


{-gameControl reads n of boards
    calls readBoard n
    readBoard calls novaJogada move until 0 is reached
    recursive readBoard until n = 0-}



    

     
     






