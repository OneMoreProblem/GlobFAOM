.
├── README.md   <----------------------------------- Этот файл
└── ejectorCase <----------------------------------- Директория с кейсом
    ├── 0       <--------------------------------------- Директория с начальными и граничными условиями
    │   ├── U   
    │   ├── k   
    │   ├── nuTilda 
    │   ├── nut     
    │   ├── p       
    │   └── s       
    ├── 0.1     <--------------------------------------- Директория результатов расчета
    │   ├── U
    │   ├── U_0
    │   ├── k
    │   ├── k_0
    │   ├── nut
    │   ├── p
    │   ├── phi
    │   ├── phi_0
    │   └── uniform
    │       ├── cumulativeContErr
    │       ├── functionObjects
    │       │   └── functionObjectProperties
    │       └── time
    ├── 3ways.png                      <--
    ├── PyFoam.blockMesh.logfile         |
    ├── PyFoamHistory                    |
    ├── PyFoamState.CurrentTime          |---------- Служебные файлы работы pyFoam
    ├── PyFoamState.LastOutputSeen       |
    ├── PyFoamState.StartedAt            |
    ├── PyFoamState.TheState           <--
    ├── clearStep.sh                   <------------ Скрипт очистки итерации
    ├── constant                       
    │   ├── polyMesh                   
    │   │   ├── boundary               
    │   │   ├── faces                  
    │   │   ├── neighbour              
    │   │   ├── owner
    │   │   └── points
    │   ├── transportProperties        <---------------- Файл свойств жидкости
    │   └── turbulenceProperties       <---------------- Файл с параметрами модели турбулентности
    ├── default.parameters             
    ├── ejectorCase.foam               <---------------- Файл для визуализации
    ├── postProcessing                 
    │   ├── fieldValueDelta1           
    │   │   └── 0                       
    │   │       └── fieldValueDelta.dat<---------------------------- Файл с результатами вычитания средних значений давления на входе и выходе
    │   ├── fieldValueDelta1.region1   
    │   │   └── 0
    │   │       └── surfaceFieldValue.dat
    │   └── fieldValueDelta1.region2   
    │       └── 0
    │           └── surfaceFieldValue.dat 
    ├── pyFoam.log                 <---------------- Лог работы pyFoam
    ├── runStep.sh                 <---------------- Скрипт запуска итерации
    ├── solver.log                 <---------------- Лог работы решателя 
    └── system                     <---------------- Директория с настройкой кейса
        ├── blockMeshDict          <-------------------- Параметры расчетной сетки
        ├── blockMeshDict.template <-------------------- Параметризованный шаблон расчетной сетки
        ├── controlDict            <-------------------- Управляющий файл
        ├── fieldValueDict         <-------------------- Файл управления постпроцессингом
        ├── fvSchemes              <-------------------- Настройки вычислителя ОДУ
        └── fvSolution             <-------------------- Настройки вычислителя СЛАУ

15 directories, 47 files

Ключевые файлы:
1) runStep.sh -- точка входа. Запуск ./runStep.sh
2) fieldValueDelta.dat -- точка выхода. 

Формат файла:

# Source1       : fieldValueDelta1.region1 -
# Source2       : fieldValueDelta1.region2  |_____ шапка
# Operation     : subtract                  |
# Time          	p                  -
0.1             	1.12191591e+05     <------ 2 значения: конечное время и результат

3) clearStep.sh -- скрипт очищающий дирректорию
