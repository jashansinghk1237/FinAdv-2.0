# --- Stage 1: Build the application ---
# Hum ek full Java JDK image ka istemaal kar rahe hain code ko build karne ke liye
FROM eclipse-temurin:17-jdk-focal AS build

WORKDIR /app
COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN ./mvnw dependency:resolve

COPY src ./src

RUN ./mvnw clean package -DskipTests

# --- Stage 2: Create the final, small image ---
# Ab hum ek choti, halki JRE (Java Runtime) image ka istemaal kar rahe hain code ko chalane ke liye
FROM eclipse-temurin:17-jre-focal

WORKDIR /app

# Build stage se sirf zaroori .jar file ko copy karein
COPY --from=build /app/target/advisor-0.0.1-SNAPSHOT.jar app.jar

# Server ko start karne ka command
ENTRYPOINT ["java", "-jar", "app.jar"]