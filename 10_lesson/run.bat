@echo off
rem ==== НАСТРОЙКА ПУТЕЙ ====
set results=.\results           rem Папка с результатами тестов
set rep_history=.\final-report\history  rem История отчетов
set report=.\final-report       rem Финальный отчет

rem ==== ОСНОВНЫЕ КОМАНДЫ ====
if exist %results% rmdir /s /q %results% 2>nul    rem Очистка
pytest --alluredir=%results%                      rem Запуск тестов

rem Копирование истории (если есть)
if exist %rep_history% (
    xcopy %rep_history% %results%\history /E /I /Y >nul
)

if exist %report% rmdir /s /q %report% 2>nul      rem Очистка отчета
allure generate %results% -o %report%             rem Генерация
allure open %report%                              rem Открытие