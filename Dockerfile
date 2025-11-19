# --- Stage 1: Build the application ---
FROM eclipse-temurin:17-jdk-focal AS build

WORKDIR /app
COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN chmod +x mvnw
RUN ./mvnw dependency:resolve

COPY src ./src

RUN ./mvnw clean package -DskipTests

# --- Stage 2: Create the final, small image ---
FROM eclipse-temurin:17-jre-focal

WORKDIR /app

# Copy the final jar
COPY --from=build /app/target/*.jar app.jar

# IMPORTANT: Expose cloud port
ENV PORT=8080

EXPOSE 8080

# Start command: Cloud runtime will override PORT if needed
ENTRYPOINT ["sh","-c","java -jar app.jar --server.port=${PORT}"]
