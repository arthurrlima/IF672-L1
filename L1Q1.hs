push :: [Int] -> Int -> [Int]
push pilha x = pilha ++ [x]

top :: [Int] -> Int
top [x]     = x
top (x:xs)  = top xs

pop :: [Int] -> [Int]
pop []      = error "Pilha Vazia"
pop [x]     = []
pop (x:xs)  = x:pop xs

checkParidade :: Int -> Int -> Bool
checkParidade x y 
 | x `mod` 2 == y `mod` 2   = True
 | otherwise                = False

doSubtracao :: Int -> Int -> Int
doSubtracao x y 
 | x >= y       = x-y
 | otherwise    = y-x

newBox :: Int -> [Int] -> [Int]
newBox n pilha
 | pilha == []                        = push pilha n
 | checkParidade (top pilha) n        = newBox (doSubtracao (top pilha) n) (pop pilha)
 | otherwise                          = push pilha n

gameControl :: IO ()
gameControl = do
    putStrLn "Enter n Games (enter 0 to finish):"
    nGames <- getInt
    newGame nGames

newGame :: Int -> IO()
newGame 0 = return()
newGame n = do
    readInput []
    newGame (n-1)


readInput :: [Int] -> IO ()
readInput ttInput = do
    box <- getInt
    if box == 0
        then formatResult ttInput
        else readInput (newBox box ttInput)

rcvBox :: [Int] -> [Int]


formatResult :: [Int] -> [String]
formatResult linesToPrint =
    -- Pilha i: length pilha top pilha
    [("Pilha"++show  ++ show (length linesToPrint) 
                ++ " " ++ show (top linesToPrint))]
    


getInt :: IO Int
getInt = read <$> getLine

main :: IO ()
main = gameControl








