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

novaJogada :: Int -> [Int] -> [Int]
novaJogada n pilha
 | pilha == []                        = push pilha n
 | checkParidade (top pilha) n        = novaJogada (doSubtracao (top pilha) n) ((pop pilha))
 | otherwise                          = push pilha n

gameControl :: IO ()
gameControl = do
    putStrLn "Enter n Games (enter 0 to finish):"
    nGames <- getInt
    readInput []

readInput :: [Int] -> IO ()
readInput ttInput = do
    move <- getInt
    if move == 0
        then printLines ttInput
        else readInput (novaJogada move ttInput)

printLines :: [Int] -> IO ()
printLines linesToPrint = do
    putStrLn "You entered the following lines:"
    print linesToPrint


getInt :: IO Int
getInt = read <$> getLine

main :: IO ()
main = gameControl









