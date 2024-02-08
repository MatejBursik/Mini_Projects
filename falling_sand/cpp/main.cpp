#include <iostream>
#include <vector>
#include <random>
#include <Windows.h>
#include <stdint.h>
#include "fall.cpp"
#include "HSLtoRGB.cpp"

using std::vector;

static bool running = true;
static void* bitmapMemory;

void draw(HDC deviceContext, vector<vector<int>> arr, int scale) {
    BITMAPINFO bitmapInfo = {};
    bitmapInfo.bmiHeader.biSize = sizeof(bitmapInfo.bmiHeader);
    bitmapInfo.bmiHeader.biWidth = (arr.size() * scale);
    bitmapInfo.bmiHeader.biHeight = (arr[0].size() * scale)*-1; // StretchDIB goes bottum up
    bitmapInfo.bmiHeader.biPlanes = 1;
    bitmapInfo.bmiHeader.biBitCount = 32;
    bitmapInfo.bmiHeader.biCompression = BI_RGB;

    if (bitmapMemory) {
        VirtualFree(bitmapMemory, NULL, MEM_RELEASE); // free bitmap memory if filled
    }

    // allocate bitmap memory
    int bmMemeorySize = ((arr.size() * scale) * (arr[0].size() * scale)) * 4;
    bitmapMemory = VirtualAlloc(NULL, bmMemeorySize, MEM_COMMIT, PAGE_READWRITE);
    
    uint8_t *row = (uint8_t *)bitmapMemory; // pointer to row in bitmap pointer
    int pitch = ((arr.size() * scale)) * 4; // bases for moving over to the next row

    // HSL to RGB converter tools
    HSL data = HSL(0, 0, 0);
    RGB value = HSLToRGB(data);

    // fill in bitmap
    for (int y = 0; y < arr.size(); y++) {
        uint8_t *pixel = (uint8_t *)row; // pointer to row pointer in bitmap pointer

        for (int x = 0; x < arr[0].size(); x++) {
            if (arr[y][x] > 0) {
                // hsl 0 - 359
                data = HSL(arr[y][x], 1, 0.5f);
                value = HSLToRGB(data);

                // blue
                *pixel = value.B;
                pixel++;

                // green
                *pixel = value.G;
                pixel++;

                // red
                *pixel = value.R;
                pixel++;

                // spacer
                *pixel = 0;
                pixel++;
            } else {
                // blue
                *pixel = 0;
                pixel++;

                // green
                *pixel = 0;
                pixel++;

                // red
                *pixel = 0;
                pixel++;

                // spacer
                *pixel = 0;
                pixel++;
            }
            
        }
        row += pitch;
    }

    // draw memory onto application
    StretchDIBits(deviceContext,
        0, 0, (arr.size() * scale), (arr[0].size() * scale),
        0, 0, (arr.size() * scale), (arr[0].size() * scale),
        bitmapMemory, &bitmapInfo, DIB_RGB_COLORS, SRCCOPY);
}

// application responses to user input
LRESULT CALLBACK WindowProcedure(HWND window, UINT msg, WPARAM wp, LPARAM lp) {
    switch (msg) {
        case WM_CLOSE:
        case WM_DESTROY:
            running = false;
            break;

        default:
            return DefWindowProc(window, msg, wp, lp);
    }
}

int CALLBACK WinMain(HINSTANCE inst, HINSTANCE prevInst, LPSTR args, int cmdshow) {
    WNDCLASS windowClass = {};
    windowClass.style = CS_OWNDC;
    windowClass.hCursor = LoadCursor(NULL, IDC_ARROW);
    windowClass.hInstance = inst;
    windowClass.lpszClassName = L"falling_sand";
    windowClass.lpfnWndProc = WindowProcedure;

    if (!RegisterClass(&windowClass)) {
        return -1;
    }

    int winX = 400;
    int winY = 400;
    int scale = 5;

    // create a window
    HWND window = CreateWindowEx(NULL, L"falling_sand", L"Falling Sand", WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_MINIMIZEBOX | WS_VISIBLE, 0, 0, winX, winY, NULL, NULL, inst, NULL);
    MSG msg = {}; // message to travel between user and application
 
    vector<vector<int>> grid = make2darrWithZero(winX / scale, winY / scale);
    int spawn = 0;
    int color = 0;

    while (running) {
        // TODO: click to spawn

        // communication between user and application
        while (PeekMessage(&msg, NULL, NULL, NULL, PM_REMOVE)) {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        
        // background grid updates
        HDC deviceContext = GetDC(window);
        draw(deviceContext, grid, scale);
        grid = fall(grid);

        if (spawn > 5) {
            if (color > 359) {
                color = 0;
            }

            grid[0][winX / scale / 10] = color;
            grid[0][winX / scale / 2] = color;

            spawn = 0;
        }

        spawn++;
        color++;
    }

    return 0;
}
