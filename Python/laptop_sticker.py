margin = 1
computerWidth, computerHeight, stickerWidth, stickerHeight = list(map(int, input().split()))

FitHorizontally = margin + stickerWidth + margin <= computerWidth
FitVertically = margin + stickerHeight + margin <= computerHeight

Fit = FitHorizontally and FitVertically
if Fit: print(1)
else: print(0)
