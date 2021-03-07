# Краткое описание предлагаемых решений на базе первичного исследования
#
**В рамках кейса рассматривались задачи**:
- Определить проблемы с данными по параметрам технологического процесса (70%)
- Определить наиболее важные этапы и параметры технологического процесса, влияющие на
качество продукции (30%)

Согласно предварительному анализу датасета по процессу плавки трансформаторной стали (см. также **Load_steel_f.ipynb**) определены проблемы с исходными данными и пути их решения.
#
### **Проблемы с исходными данными и пути их решения**

#
**1 Неполнота данных** присутствует по следующим факторам (частичное или полное отсутствие данных, дубликаты, некорректный формат данных):
- **X0['Поступление_в_технологическую_секцию']**
- **X0['Выезд_из_технологической_секции']**

- **X0['Начало непрерывного отжига']**
- **X0['Окончание непрерывного отжига']**

- **X0['Точка_росы_Этап1_зона1']**
- **X0['Точка_росы_Этап1_зона2']**
- **X0['CO_Этап1_зона1']**

где
- **X0** - массив факторов процесса плавки
- **Y0** - результирующий признак **['Удельные_потери']** в стали

**Пути решения**:

По датам и другим численным параметрам заполнить пропуски, исходя из (и/или) 

**a)** знания технологии процесса (техкарты, информация от специалистов, АСУТП, данные из OPC-серверов, журналов и др.)

**b)** на базе дополнительных моделей, построенных на данных без пропусков, даже если они отличаются по другим параметрам от сценариев с пропусками (на базе критериев подобия)

**c)** на основе моделей интерполяции, если это возможно по структуре и содержанию временного ряда

**d)** на основе физических моделей именно для данных параметров подпроцессов процесса плавки (при наличии, изученности вопроса) 

**e)** замена параметров производными, известными

#
**2** Всё множество факторов имеет как количественное, так и **качественное содержание**

- Качественные признаки:

-- **X0['ШОС']**

-- **X0['Толщина_перед_смоткой']** - условно качественный может быть преобразован в количественный при определенной трансформации или использоваться как класс

**Пути решения**:

**a)** оцифровка, рассматривать как фичу

**b)** оцифровка, рассматривать как класс для дробления метамодели на подмодели

#
**3 Общие проблемы и пути решения**

- **неоднородные данные** - использовать методы оценки однородности выборок и исключения выбросов, сглаживание, а также техники сведения к однородности

- недостаток в данных, **проблема репрезентативности** на практике - обогащение данных по аналогам и др.

- разделение данных на **группы** (кластеры) для достижения большей точности

#
### **Общие ТОП-20 признаков**

<details>
  
<summary>**Признак - значимость по коэф. детерминации** </summary>

<ul>
<li>Удельные_потери	- 1.000000</li>
<li>Средние_магнитные_потери -	0.797610</li>
<li>F	- 0.488820</li>
<li>Al	- 0.472760</li>
<li>Коэффициент_свойств_стали	- 0.447074</li>
<li>Cr	- 0.386131</li>
<li>Азот_среднее	- 0.370441</li>
<li>Азот_начало	- 0.274943</li>
<li>Азот_конец	- 0.273847</li>
<li>Толщина_МС	- 0.260606</li>
<li>Si	- 0.221579</li>
<li>C	- 0.207444</li>
<li>Углерод_конец	- 0.201244</li>
<li>Углерод_среднее	- 0.183379</li>
<li>Sn	- 0.177957</li>
<li>Датчик_механических_свойств	- 0.175156</li>
<li>Кислород_начало	- 0.153553</li>
<li>T_Этап1_зона4	- 0.148593</li>
<li>H2_Этап4_зона1	- 0.146318</li>
<li>T_Этап1_зона5	- 0.140490</li>

</ul>

</details>


**Примечание:** 

- использовалась первичная обработка данных (удаление дубликатов, чистка пустых и нечисловых значений, отсечение качественных признаков на данном этапе)

- модель предварительного анализа строилась на всем множестве признаков без кластеризации по группам, оценки однородности и восполнения недостающих данных

#
### **Сводная таблица по сформированным моделям и их точности**

**Модель** - **Коэф. детерминации**
```
LinearRegression : ≈ 1.00
KNeighborsRegressor : 0.916157
RandomForestRegressor : 0.996736
SVR : -0.031550
```

**Примечание:** 
- LinearRegression - МНК-регрессия
- KNeighborsRegressor - Метод ближайших соседей
- RandomForestRegressor - регрессор на базе случайных деревьев
- SVR - метод опорных векторов (default - ’rbf’)

### 
Осуществлен переход к следующему обозначению факторов модели плавки:
Xi - факторы модели (процесса)
Y - результирующий признак dataset['Удельные_потери'] 

#
### **Общие направления работ**

1. В перспективе список моделей должен быть расширен в рамках единого алгоритма поиска наилучшего решения (по степени сложности и многопараметричности задачи) с использованием ML. 
2. Поиск наилучшей модели, необходимо осуществлять также с учетом оптимальной настройки гиперпараметров
3. Необходимо учитывать кодированные значения качественных признаков и физическую модель процесса плавки для уточнения (при ее наличии)
4. Проработка архитектуры и средств реализации сервиса для расчета модели плавки трансформаторной стали, безопасность передачи данных, разделение прав.

**Примечание:** 

- усложнение только в случае необходимости

- анализ по моделям подробнее в **Load_steel_f.ipynb**

#
**PS**: таков список работ, друзья, и видение ситуации - **драфт решения** кейса как примера